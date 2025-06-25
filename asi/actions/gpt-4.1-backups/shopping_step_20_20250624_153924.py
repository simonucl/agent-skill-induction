from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None


def access_order_details(account_id: str, order_view_id: str):
    """
    Navigate to account page and view a specific order's details.

    Args:
        account_id: The ID of the "My Account" link.
        order_view_id: The ID to click and view the specific order.

    Returns:
        None

    Examples:
        access_order_details('227', '1553')
    """
    click(account_id)
    click(order_view_id)

def open_reviews_and_next_page(reviews_tab_id: str, next_page_id: str):
    """
    Opens the reviews tab and navigates to the next review page.
    
    Args:
        reviews_tab_id: The element ID for the reviews tab.
        next_page_id: The element ID for the next page of reviews.
    
    Returns:
        None
    
    Examples:
        open_reviews_and_next_page('1688', '2081')
    
    """
    click(reviews_tab_id)
    click(next_page_id)

def subscribe_newsletter(email_field_id: str, subscribe_button_id: str, email_address: str):
    """
    Subscribes to a newsletter by filling the email input and clicking the subscribe button.

    Args:
        email_field_id: The element ID of the email input textbox.
        subscribe_button_id: The element ID of the subscribe button.
        email_address: The email address to use for subscribing.

    Returns:
        None

    Examples:
        subscribe_newsletter('1964', '1966', 'sample@email.com')
    """
    fill(email_field_id, email_address)
    click(subscribe_button_id)

def search_and_add_to_wishlist(category_id: str, subcategory_id: str, advanced_search_id: str, name_field_id: str, search_button_id: str, product_name: str, wishlist_button_id: str):
    """
    Navigates through categories, performs an advanced product search, and adds the first relevant result to the wish list.

    Args:
        category_id: The ID of the main category to click (e.g., 'Office Products').
        subcategory_id: The ID of the subcategory to filter products (e.g., 'Office Furniture & Lighting').
        advanced_search_id: The ID for the advanced search feature.
        name_field_id: The element ID for the product name input field.
        search_button_id: The ID for the search/submit button.
        product_name: The name of the product to search for.
        wishlist_button_id: The ID of the "Add to Wish List" button for the relevant product.

    Returns:
        None

    Examples:
        search_and_add_to_wishlist('836', '1925', '392', '1488', '1520', 'white computer desk', '1542')
    """
    click(category_id)
    click(subcategory_id)
    click(advanced_search_id)
    fill(name_field_id, product_name)
    click(search_button_id)
    click(wishlist_button_id)