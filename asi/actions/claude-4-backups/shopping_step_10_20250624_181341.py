from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None

def search_and_sort_products(search_box_id: str, search_button_id: str, product_name: str, sort_dropdown_id: str, sort_option: str):
    """Search for a product and sort the results by specified criteria.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button
        product_name: The name of the product to search for
        sort_dropdown_id: The ID of the sort dropdown menu
        sort_option: The sorting option to apply (e.g., "Price", "Relevance")
        
    Returns:
        None
        
    Examples:
        search_and_sort_products('386', '391', 'iphone 12 phone case', '1500', 'Price')
        search_and_sort_products('search_box', 'search_btn', 'laptop bags', 'sort_menu', 'Rating')
    """
    fill(search_box_id, product_name)
    click(search_button_id)
    select_option(sort_dropdown_id, sort_option)

def search_product(search_id: str, product_query: str):
    """Search for a product using the search functionality.
    
    Args:
        search_id: The ID of the search input field or button
        product_query: The search query string for the product
        
    Returns:
        None
        
    Examples:
        search_product('567', 'Nintendo Switch game card storage case')
        search_product('179', 'Nintendo Switch game card storage')
    """
    click(search_id)
    fill(search_id, product_query)
    keyboard_press('Enter')

def navigate_to_account_orders(account_link_id: str, view_all_id: str):
    """Navigate from homepage to the order history page.
    
    Args:
        account_link_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link
        
    Returns:
        None
        
    Examples:
        navigate_to_account_orders('227', '1742')
    """
    click(account_link_id)
    click(view_all_id)

def navigate_reviews_and_search(reviews_tab_id: str, next_page_id: str):
    """Navigate to reviews section and browse through review pages.
    
    Args:
        reviews_tab_id: The ID of the reviews tab
        next_page_id: The ID of the next page button in reviews
        
    Returns:
        None
        
    Examples:
        navigate_reviews_and_search('1687', '2081')
    """
    click(reviews_tab_id)
    click(next_page_id)
    click('2176')