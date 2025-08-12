import pytest
import random
import warnings

from mythic_container.MythicGoRPC.tags.msgs import (
    MythicRPCTagTypeData, MythicRPCTagData, MythicRPCTagCreateMessageResponse, MythicRPCTagSearchMessageResponse,
    MythicRPCTagSearchMessage)

rand = random.Random()  # Set the seed for consistent testing


# Example RPC messages to create the object
@pytest.fixture
def rpc_tag_type_data():
    return {
        "id": rand.randint(1, 999),
        "name": "test_name",
        "description": "test_desc",
        "color": "test_color",
        "operation_id": rand.randint(1, 999),
    }


@pytest.fixture
def rpc_tag_data(rpc_tag_type_data):
    return {
        "id": rand.randint(1, 999),
        "tagtype_id": rand.randint(1, 999),
        "tagtype": rpc_tag_type_data,
        "data": {"rand_key": "abc"},
        "url": "http://example.com",
        "source": "test_source",
        "task_id": rand.randint(1, 999),
        "file_id": rand.randint(1, 999),
        "credential_id": rand.randint(1, 999),
        "mythic_tree_id": rand.randint(1, 999)
    }

@pytest.fixture
def rpc_tag_create_response_data(rpc_tag_data):
    return {
        "success": rand.randint(0, 1) == 1,  # convert to a bool by flipping between 0 and 1
        "error": "an error message",
        "tag": rpc_tag_data
    }

@pytest.fixture
def rpc_tag_search_response_data(rpc_tag_data):
    return {
        "success": rand.randint(0, 1) == 1,  # convert to a bool by flipping between 0 and 1
        "error": "an error message",
        "tags": [rpc_tag_data]
    }


@pytest.fixture
def rpc_tag_search_data():
    return {
        "task_id": rand.randint(1, 999),
        "search_tag_id": rand.randint(1, 999),
        "search_tag_task_id": rand.randint(1, 999),
        "search_tag_file_id": rand.randint(1, 999),
        "search_tag_credential_id": rand.randint(1, 999),
        "search_tag_mythictree_id": rand.randint(1, 999),
        "search_tag_source": "test_tag_source",
        "search_tag_data": "test_tag_data",
        "search_tag_url": "test_tag_url"
    }


def test_MythicRPCTagTypeData(rpc_tag_type_data):
    """Test that MythicRPCTagTypeData is created correctly"""
    tag_obj = MythicRPCTagTypeData(**rpc_tag_type_data)
    assert rpc_tag_type_data["id"] == tag_obj.id, "The 'id' property differs from expected"
    assert rpc_tag_type_data["name"] == tag_obj.name, "The 'name' property differs from expected"
    assert rpc_tag_type_data["description"] == tag_obj.description, "The 'description' property differs from expected"
    assert rpc_tag_type_data["color"] == tag_obj.color, "The 'color' property differs from expected"
    assert rpc_tag_type_data["operation_id"] == tag_obj.operation_id, "The 'operation_id' property differs from expected"

    assert rpc_tag_type_data == tag_obj.to_json(), "Output from 'to_json' does not match expected output"


def test_MythicRPCTagData(rpc_tag_data):
    """Test that MythicRPCTagData is created correctly"""
    tag_obj = MythicRPCTagData(**rpc_tag_data)
    assert rpc_tag_data["id"] == tag_obj.id, "The 'id' property differs from expected"
    assert rpc_tag_data["tagtype_id"] == tag_obj.tagtype_id, "The 'tagtype_id' property differs from expected"
    assert MythicRPCTagTypeData(**rpc_tag_data["tagtype"]) == tag_obj.tagtype, "The 'tagtype' property differs from expected"
    assert rpc_tag_data["data"] == tag_obj.data, "The 'data' property differs from expected"
    assert rpc_tag_data["url"] == tag_obj.url, "The 'url' property differs from expected"
    assert rpc_tag_data["source"] == tag_obj.source, "The 'source' property differs from expected"
    assert rpc_tag_data["task_id"] == tag_obj.task_id, "The 'task_id' property differs from expected"
    assert rpc_tag_data["file_id"] == tag_obj.file_id, "The 'file_id' property differs from expected"
    assert rpc_tag_data["credential_id"] == tag_obj.credential_id, "The 'credential_id' property differs from expected"
    assert rpc_tag_data["mythic_tree_id"] == tag_obj.mythic_tree_id, "The 'mythic_tree_id' property differs from expected"

    assert rpc_tag_data == tag_obj.to_json(), "Output from 'to_json' does not match expected output"


def test_MythicRPCTagData_with_empty_data():
    """Test that passing None for 'data' creates an empty dict"""
    empty_data_tag_obj = MythicRPCTagData(data=None)
    assert empty_data_tag_obj.data == {}
    assert empty_data_tag_obj.data is not None


def test_MythicRPCTagData_with_tagtype_dict(rpc_tag_type_data):
    """Test that if 'tagtype' is a dict it is converted to MythicRPCTagTypeData"""
    tag_type_obj = MythicRPCTagTypeData(**rpc_tag_type_data)
    tag_type_dict_tag_obj = MythicRPCTagData(tagtype=rpc_tag_type_data)
    assert tag_type_dict_tag_obj.tagtype != tag_type_dict_tag_obj
    assert tag_type_dict_tag_obj.tagtype == tag_type_obj

    # Test that a MythicRPCTagTypeData is not converted again
    tag_obj = MythicRPCTagData(tagtype=tag_type_obj)
    assert tag_obj.tagtype == tag_type_obj
    assert isinstance(tag_obj.tagtype, MythicRPCTagTypeData)


def test_MythicRPCTagCreateMessageResponse(rpc_tag_create_response_data):
    tag_obj = MythicRPCTagCreateMessageResponse(**rpc_tag_create_response_data)

    assert rpc_tag_create_response_data["success"] == tag_obj.success
    assert rpc_tag_create_response_data["error"] == tag_obj.error
    assert MythicRPCTagData(**rpc_tag_create_response_data["tag"]) == tag_obj.tag

    assert tag_obj.to_json() == rpc_tag_create_response_data

def test_MythicRPCTagCreateMessageResponse_with_tag_dict(rpc_tag_data):
    # Test that if 'tag' is a dict it is converted to MythicRPCTagData
    tag_data_obj = MythicRPCTagData(**rpc_tag_data)
    tag_obj = MythicRPCTagCreateMessageResponse(tag=rpc_tag_data)
    assert tag_obj.tag != rpc_tag_data
    assert tag_obj.tag == tag_data_obj

    # Test that a MythicRPCTagData is not converted again
    tag_obj = MythicRPCTagCreateMessageResponse(tag=tag_data_obj)
    assert tag_obj.tag == tag_data_obj
    assert isinstance(tag_obj.tag, MythicRPCTagData)


def test_MythicRPCTagSearchMessageResponse(rpc_tag_search_response_data):
    tag_obj = MythicRPCTagSearchMessageResponse(**rpc_tag_search_response_data)

    assert rpc_tag_search_response_data["success"] == tag_obj.success
    assert rpc_tag_search_response_data["error"] == tag_obj.error
    assert [MythicRPCTagData(**tag) for tag in rpc_tag_search_response_data["tags"]] == tag_obj.tags

    assert tag_obj.to_json() == rpc_tag_search_response_data


def test_MythicRPCTagSearchMessageResponse_with_tag_dict(rpc_tag_data):
    # Test that if 'tag' is a dict it is converted to MythicRPCTagData
    tag_data_obj = MythicRPCTagData(**rpc_tag_data)
    tag_obj = MythicRPCTagSearchMessageResponse(tags=[rpc_tag_data])
    assert tag_obj.tags != [rpc_tag_data]
    assert tag_obj.tags == [tag_data_obj]

    # Test that a MythicRPCTagData is not converted again
    tag_obj = MythicRPCTagSearchMessageResponse(tags=[tag_data_obj])
    assert tag_obj.tags == [tag_data_obj]
    assert isinstance(tag_obj.tags, list)


def test_MythicRPCTagSearchMessage(rpc_tag_search_data):
    tag_obj = MythicRPCTagSearchMessage(**rpc_tag_search_data)

    assert rpc_tag_search_data["task_id"] == tag_obj.task_id
    assert rpc_tag_search_data["search_tag_id"] == tag_obj.search_tag_id
    assert rpc_tag_search_data["search_tag_task_id"] == tag_obj.search_tag_task_id
    assert rpc_tag_search_data["search_tag_file_id"] == tag_obj.search_tag_file_id
    assert rpc_tag_search_data["search_tag_credential_id"] == tag_obj.search_tag_credential_id
    assert rpc_tag_search_data["search_tag_mythictree_id"] == tag_obj.search_tag_mythictree_id
    assert rpc_tag_search_data["search_tag_source"] == tag_obj.search_tag_source
    assert rpc_tag_search_data["search_tag_data"] == tag_obj.search_tag_data
    assert rpc_tag_search_data["search_tag_url"] == tag_obj.search_tag_url

    assert tag_obj.to_json() == rpc_tag_search_data


# These tests can be removed once the deprecated values are removed
def test_deprecated_warnings_for_MythicRPCTagTypeData():
    """Test that using old variables are deprecated, but still usable"""
    tag_obj = MythicRPCTagTypeData()

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.ID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.id == tag_obj.ID, "The deprecated 'ID' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Name
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.name == tag_obj.Name, "The deprecated 'Name' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Description
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.description == tag_obj.Description, "The deprecated 'Description' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Color
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.color == tag_obj.Color, "The deprecated 'Color' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.OperationID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.operation_id == tag_obj.OperationID, "The deprecated 'OperationID' property differs from expected"


def test_deprecated_warnings_for_MythicRPCTagData():
    """Test that using old variables are deprecated, but still usable"""
    tag_obj = MythicRPCTagData()

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.ID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.id == tag_obj.ID, "The deprecated 'ID' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.TagTypeID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.tagtype_id == tag_obj.TagTypeID, "The deprecated 'TagTypeID' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.TagType
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.tagtype == tag_obj.TagType, "The deprecated 'TagType' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Data
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.data == tag_obj.Data, "The deprecated 'Data' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.URL
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.url == tag_obj.URL, "The deprecated 'URL' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Source
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.source == tag_obj.Source, "The deprecated 'Source' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.TaskID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.task_id == tag_obj.TaskID, "The deprecated 'TaskID' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.FileID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.file_id == tag_obj.FileID, "The deprecated 'FileID' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.CredentialID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.credential_id == tag_obj.CredentialID, "The deprecated 'CredentialID' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.MythicTreeID
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.mythic_tree_id == tag_obj.MythicTreeID, "The deprecated 'MythicTreeID' property differs from expected"


def test_deprecated_warnings_for_MythicRPCTagCreateMessageResponse():
    """Test that using old variables are deprecated, but still usable"""
    tag_obj = MythicRPCTagCreateMessageResponse()

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Success
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.success == tag_obj.Success, "The deprecated 'Success' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Error
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.error == tag_obj.Error, "The deprecated 'Error' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Tag
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.tag == tag_obj.Tag, "The deprecated 'Tag' property differs from expected"


def test_deprecated_warnings_for_MythicRPCTagCreateMessageResponse():
    """Test that using old variables are deprecated, but still usable"""
    tag_obj = MythicRPCTagSearchMessageResponse()

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Success
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.success == tag_obj.Success, "The deprecated 'Success' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Error
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.error == tag_obj.Error, "The deprecated 'Error' property differs from expected"

    # Assert that a UserWarning is raised from using a deprecated method
    with pytest.warns(UserWarning):
        tag_obj.Tags
    # Assert that deprecated and current properties are equal
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert tag_obj.tags == tag_obj.Tags, "The deprecated 'Tags' property differs from expected"
