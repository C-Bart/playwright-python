def test_private_chat_conversation(login_set_up_for_chat):
    page1, page2 = login_set_up_for_chat

    # User from page1 send message
    page1.click()

    # User from page2 check the message and reply
    page2.click()
