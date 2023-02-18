import os
from typing import Generator

import pytest


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "ignore_https_errors": True
#     }


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {
#             "width": 400,
#             "height": 400
#         }
#     }


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     iphone_11 = playwright.devices['iPhone 11 Pro']
#     return {
#         **browser_context_args,
#         **iphone_11
#     }


# @pytest.fixture(scope="session")
# def context(
#         browser_type,
#         browser_type_launch_args,
#         browser_context_args
# ):
#     context = browser_type.launch_persistent_context(
#         "./foobar",
#         **{
#             **browser_type_launch_args,
#             **browser_context_args,
#             "locale": "de-DE"
#         }
#     )
#     yield context
#     context.close()
from playwright.sync_api import Playwright, APIRequestContext, expect


def _get_env_var(varname: str) -> str:
    value = os.getenv(varname)
    assert value, f'{varname} is not set'
    return value


@pytest.fixture(scope="session")
def gh_user() -> str:
    return _get_env_var("GITHUB_USERNAME")


@pytest.fixture(scope="session")
def gh_password() -> str:
    return _get_env_var("GITHUB_PASSWORD")


@pytest.fixture(scope="session")
def gh_token() -> str:
    return _get_env_var("GITHUB_TOKEN")


@pytest.fixture(scope="session")
def gh_project_name() -> str:
    return _get_env_var("GITHUB_PROJECT")


@pytest.fixture(scope="session")
def gh_context(playwright: Playwright, gh_token: str) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {gh_token}"
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def gh_project(gh_context: APIRequestContext, gh_user: str, gh_project_name: str) -> dict:
    resource = f'/users/{gh_user}/projects'
    response = gh_context.get(resource)
    expect(response).to_be_ok()
    name_match = lambda x: x['name'] == gh_project_name
    filtered = filter(name_match, response.json())
    project = list(filtered)[0]
    assert project
    return project


@pytest.fixture()
def project_columns(gh_context: APIRequestContext, gh_project: dict) -> list[dict]:
    response = gh_context.get(gh_project['columns_url'])
    expect(response).to_be_ok()
    columns = response.json()
    assert len(columns) >= 2
    return columns


@pytest.fixture()
def project_column_ids(project_columns: list[dict]) -> list[str]:
    return list(map(lambda x: x['id'], project_columns))
