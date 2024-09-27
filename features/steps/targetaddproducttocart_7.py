def test_logged_out_user_can_access_sign_in(driver):
    # Navigate to Target main page
    driver.get("https://www.target.com")

    # Create an instance of MainPage and click the header "Sign In" button
    main_page = MainPage(driver)
    main_page.click_header_sign_in()

    # Create an instance of SignInMenu and click the "Sign In" link from the menu
    sign_in_menu = SignInMenu(driver)
    sign_in_menu.click_menu_sign_in()

    # Create an instance of SignInPage to verify that the Sign In form is displayed
    sign_in_page = SignInPage(driver)
    assert sign_in_page.is_sign_in_form_opened(), "Sign In form was not opened."
