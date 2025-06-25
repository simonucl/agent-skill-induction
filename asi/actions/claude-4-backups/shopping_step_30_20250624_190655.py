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

def search_product_and_get_results(search_box_id: str, search_button_id: str, product_name: str):
    """Search for a product and navigate to the results page to view pricing and availability.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button
        product_name: The name of the product to search for
        
    Returns:
        None
        
    Examples:
        search_product_and_get_results('389', '394', 'Canon photo printer')
        search_product_and_get_results('search_box', 'search_btn', 'laptop bags')
    """
    fill(search_box_id, product_name)
    click(search_button_id)

def search_and_navigate_to_product(search_box_id: str, search_button_id: str, product_name: str, product_link_id: str):
    """Search for a product and navigate to its detailed product page.
    
    Args:
        search_box_id: The ID of the search input field
        search_button_id: The ID of the search button  
        product_name: The name of the product to search for
        product_link_id: The ID of the product link in search results
        
    Returns:
        None
        
    Examples:
        search_and_navigate_to_product('505', '510', 'Amazon Echo Dot 3rd generation', '1751')
        search_and_navigate_to_product('search_box', 'search_btn', 'iPhone case', 'product_link')
    """
    fill(search_box_id, product_name)
    click(search_button_id)
    click(product_link_id)

def navigate_to_order_history(account_link_id: str, view_all_id: str):
    """Navigate from homepage to the complete order history page.
    
    Args:
        account_link_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link
        
    Returns:
        None
        
    Examples:
        navigate_to_order_history('227', '1690')
    """
    click(account_link_id)
    click(view_all_id)

def browse_order_pages(page_ids: list):
    """Browse through multiple pages of order history.
    
    Args:
        page_ids: A list of page link IDs to navigate through
        
    Returns:
        None
        
    Examples:
        browse_order_pages(['1766', '1774', '1778'])
    """
    for page_id in page_ids:
        click(page_id)

def navigate_to_address_management(account_id: str, manage_addresses_id: str):
    """Navigate from homepage to the address management page.
    
    Args:
        account_id: The ID of the "My Account" link
        manage_addresses_id: The ID of the "Manage Addresses" link
        
    Returns:
        None
        
    Examples:
        navigate_to_address_management('227', '1658')
    """
    click(account_id)
    click(manage_addresses_id)

def update_billing_address(change_address_id: str, street: str, city: str, state: str, zip_code: str, save_button_id: str):
    """Update billing address with new information.
    
    Args:
        change_address_id: The ID of the "Change Billing Address" link
        street: The new street address
        city: The new city name
        state: The new state name
        zip_code: The new ZIP/postal code
        save_button_id: The ID of the "Save Address" button
        
    Returns:
        None
        
    Examples:
        update_billing_address('1648', '987 Sycamore Circle', 'Philadelphia', 'Pennsylvania', '19102', '2026')
    """
    click(change_address_id)
    fill('1674', street)
    select_option('1939', state)
    fill('2011', city)
    fill('2016', zip_code)
    click(save_button_id)