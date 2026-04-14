import json
from dotenv import load_dotenv
from langfuse import get_client

load_dotenv()

langfuse = get_client()

query = json.dumps({
    "view": "traces",
    "metrics": [{"measure": "totalCost", "aggregation": "sum"}, {"measure": "count", "aggregation": "count"}],
    "dimensions": [{"field": "tags"}],
    "filters": [],
    "fromTimestamp": "2026-04-12T23:20:10Z",
    "toTimestamp": "2026-04-12T23:38:35Z"
})

response = langfuse.api.legacy.metrics_v1.metrics(query=query)
print(response)


#     "fromTimestamp": "2026-04-13T00:31:00Z",
#     "toTimestamp": "2026-04-13T00:41:30Z"
# data=[{'tags': ['AF_abcd_gpt-4o'], 'sum_totalCost': 1.000412499955, 'count_count': '300'}]

#     "fromTimestamp": "2026-04-12T22:52:15Z",
#     "toTimestamp": "2026-04-12T23:03:15Z"
# data=[{'tags': ['RF_abcd_gpt-4o'], 'sum_totalCost': 0.998722499954, 'count_count': '300'}]

#     "fromTimestamp": "2026-04-13T00:13:10Z",
#     "toTimestamp": "2026-04-13T00:22:05Z"
# data=[{'tags': ['NR_abcd_gpt-4o'], 'sum_totalCost': 0.738172499992, 'count_count': '300'}]

#     "fromTimestamp": "2026-04-12T23:04:00Z",
#     "toTimestamp": "2026-04-12T23:27:10Z"
# data=[{'tags': ['RF_abcd_gpt-5.4'], 'sum_totalCost': 1.100382499964, 'count_count': '300'}, {'tags': ['AF_abcd_gpt-5.4'], 'sum_totalCost': 1.091697499957, 'count_count': '300'}, {'tags': ['NR_abcd_gpt-5.4'], 'sum_totalCost': 0.771687499962, 'count_count': '300'}, {'tags': ['NR_abcd_gpt-4o'], 'sum_totalCost': 0.0023125, 'count_count': '2'}]

#     "fromTimestamp": "2026-04-12T23:27:00Z",
#     "toTimestamp": "2026-04-13T00:01:25Z"
# data=[{'tags': ['RF_abcd_o3'], 'sum_totalCost': 1.05550599993, 'count_count': '300'}, {'tags': ['AF_abcd_o3'], 'sum_totalCost': 1.044015999935, 'count_count': '295'}, {'tags': ['NR_abcd_o3'], 'sum_totalCost': 0.866641999943, 'count_count': '300'}, {'tags': ['NR_abcd_gpt-5.4'], 'sum_totalCost': 0.018482499999, 'count_count': '7'}]

