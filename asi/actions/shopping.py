from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None

def search_product(search_bar_id: str, product_name: str):
    """Search for a product using the search bar.
    
    Args:
        search_bar_id: The ID of the search bar element
        product_name: The name or keywords of the product to search for
        
    Returns:
        None
        
    Examples:
        search_product('567', 'Nintendo Switch game card storage case')
        search_product('179', 'Nintendo Switch game card storage')
    """
    click(search_bar_id)
    fill(search_bar_id, product_name)
    keyboard_press('Enter')

def navigate_to_account_orders(account_link_id: str, view_all_id: str):
    """Navigate from homepage to the complete order history page.
    
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

def navigate_review_pages(reviews_tab_id: str, page_2_id: str, page_1_id: str):
    """Navigate through review pages to examine all available reviews.
    
    Args:
        reviews_tab_id: The ID of the Reviews tab
        page_2_id: The ID of the page 2 navigation link
        page_1_id: The ID of the page 1 navigation link
        
    Returns:
        None
        
    Examples:
        navigate_review_pages('1573', '1967', '2062')
    """
    click(reviews_tab_id)
    click(page_2_id)
    click(page_1_id)