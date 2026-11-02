"""
MCP Server for Critical Flicker Fusion Frequency (CFFF) & Cortical Arousal.
Exposes JSON-RPC endpoints for computing CFFF thresholds, hysteresis, and CNS fatigue indices.
"""

import json
import sys
from client import CriticalFlickerFusionClient

client = CriticalFlickerFusionClient()


def handle_request(request: dict) -> dict:
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_cfff_thresholds",
                        "description": "Calculates Critical Flicker Fusion Frequency (CFFF) in Hz, threshold hysteresis, and Cortical Arousal Index from ascending/descending trials.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "ascending_trials_hz": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "Frequencies in Hz where flicker fused into steady light"
                                },
                                "descending_trials_hz": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "Frequencies in Hz where steady light first exhibited visible flicker"
                                },
                                "baseline_cfff_hz": {
                                    "type": "number",
                                    "default": 38.0,
                                    "description": "User baseline rested CFFF threshold in Hz"
                                }
                            },
                            "required": ["ascending_trials_hz", "descending_trials_hz"]
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "evaluate_cfff_thresholds":
            res = client.evaluate_cfff_thresholds(
                ascending_trials_hz=args.get("ascending_trials_hz", []),
                descending_trials_hz=args.get("descending_trials_hz", []),
                baseline_cfff_hz=args.get("baseline_cfff_hz", 38.0)
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
            }

        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method {tool_name} not found"}
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32600, "message": "Invalid Request"}
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
