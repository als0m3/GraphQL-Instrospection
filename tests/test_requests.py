import unittest
from unittest.mock import patch
from src.request import graphql_request

class RequestTests(unittest.TestCase):
    @patch("src.request.requests.post")
    def test_posts_query_variables_and_auth(self, post):
        post.return_value.json.return_value = {"data": {"hello": "world"}}
        result = graphql_request("https://example.com/graphql", "query { hello }", "test-token", {"limit": 1})
        self.assertEqual(result["data"]["hello"], "world")
        self.assertEqual(post.call_args.kwargs["json"]["variables"], {"limit": 1})
        self.assertEqual(post.call_args.kwargs["headers"]["Authorization"], "Bearer test-token")
