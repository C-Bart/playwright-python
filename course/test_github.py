import time

from playwright.sync_api import expect


def test_create_project_card(gh_context, project_column_ids) -> None:
    now = time.time()
    card_name = f"A new task at {now}"

    logs = open("log.txt", "w")

    c_response = gh_context.post(
        f'projects/columns/{project_column_ids[0]}/cards',
        data={'note': card_name}
    )

    logs.write("\n Column IDs: " + str(project_column_ids))
    logs.write("\n" + c_response.json()['note'])

    expect(c_response).to_be_ok()
    assert c_response.json()['note'] == card_name

    card_id = c_response.json()['id']

    logs.write("\n Created response: " + str(c_response.json()))

    r_response = gh_context.get(f'/projects/columns/cards/{card_id}')

    logs.write("\n Retrieved response: " + str(r_response.json()))
    expect(r_response).to_be_ok()
    assert r_response.json() == c_response.json()


def test_move_card(gh_context, gh_project, project_column_ids, page, gh_user, gh_password) -> None:
    logs = open("log2.txt", "w")
    source_col = project_column_ids[0]
    dist_col = project_column_ids[1]
    now = time.time()
    card_name = f"Move this card at: {now}"

    c_response = gh_context.post(
        f"/projects/columns/{source_col}/cards",
        data={'note': card_name}
    )
    expect(c_response).to_be_ok()

    page.goto('https://github.com')
    page.locator('id=login_field').fill(gh_user)
    page.locator('id=password').fill(gh_password)
    page.locator('input[name="commit"]').click()

    page.goto(f'https://github.com/users/{gh_user}/projects/{gh_project["number"]}')
    logs.write("\n Projects Data: " + str(gh_project))

    card_col = f"//div[@id='columns-cards-{source_col}//p[contains(text(),'{card_name}']"
    expect(page.locator(card_col)).to_be_visible()

    page.drag_and_drop(f'text="{card_name}"', f'id=column-cards-{dist_col}')

    card_col = f"//div[@id='columns-cards-{dist_col}//p[contains(text(),'{card_name}']"
    expect(page.locator(card_col)).to_be_visible()

    card_id = c_response.json()['id']
    r_response = gh_context.get(f'/projects/columns/cards/{card_id}')
    expect(r_response).to_be_ok()
    assert r_response.json()['column_url'].endswith(str(dist_col))
