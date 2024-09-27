def test_sign_in_page_access(driver):
    main_page = MainPage(driver)
    main_page.click_sign_in()

    sign_in_menu = SignInMenu(driver)
    sign_in_menu.click_sign_in()

    assert "Sign In" in driver.title  # Verify the Sign-In form opened
