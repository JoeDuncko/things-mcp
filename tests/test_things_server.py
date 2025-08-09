import asyncio
from unittest.mock import patch
import uuid

import things_server


def test_add_heading_failure():
    with patch('things.get') as mock_get, \
         patch('url_scheme.execute_url') as mock_exec, \
         patch('uuid.uuid4', return_value=uuid.UUID('12345678-1234-5678-1234-567812345678')):
        mock_get.return_value = {'type': 'project'}
        mock_exec.side_effect = RuntimeError('invalid json')
        result = asyncio.run(things_server.add_heading('project-id', 'Title'))
        assert 'invalid json' in result
        assert 'things:///json' in result


def test_delete_heading_failure():
    with patch('things.get') as mock_get, \
         patch('things.todos') as mock_todos, \
         patch('url_scheme.execute_url') as mock_exec:
        mock_get.return_value = {'type': 'heading'}
        mock_todos.return_value = []
        mock_exec.side_effect = RuntimeError('invalid json')
        result = asyncio.run(things_server.delete_heading('heading-id'))
        assert 'invalid json' in result
        assert 'things:///json' in result
