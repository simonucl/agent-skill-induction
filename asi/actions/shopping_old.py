from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None


def search_product_and_submit(search_bar_id: str, product_name: str):
    """Search for a product using the search bar and submit the search.
    
    Args:
        search_bar_id: The ID of the search bar element
        product_name: The name of the product to search for
        
    Returns:
        None
        
    Examples:
        search_product_and_submit('567', 'Nintendo Switch game card storage case')
        search_product_and_submit('179', 'Nintendo Switch game card storage')
    """
    click(search_bar_id)
    fill(search_bar_id, product_name)
    keyboard_press('Enter')

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
    """Navigate from homepage to order history page.
    
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

def access_product_reviews(reviews_tab_id: str):
    """Navigate to the reviews section of a product page.
    
    Args:
        reviews_tab_id: The ID of the reviews tab element
        
    Returns:
        None
        
    Examples:
        access_product_reviews('1689')
    """
    click(reviews_tab_id)
    scroll(0, 300)

def navigate_review_pages(page_id: str):
    """Navigate between different pages of reviews.
    
    Args:
        page_id: The ID of the page navigation element
        
    Returns:
        None
        
    Examples:
        navigate_review_pages('2199')
        navigate_review_pages('2483')
    """
    click(page_id)
    scroll(0, -200)

def search_product(search_bar_id, product_name):
    """Search for a product using the search bar.
    
    Args:
        search_bar_id: The ID of the search bar element
        product_name: The name or keywords to search for
        
    Returns:
        None
        
    Examples:
        search_product('567', 'Nintendo Switch game card storage case')
        search_product('179', 'Nintendo Switch game card storage')
    """
    click(search_bar_id)
    fill(search_bar_id, product_name)
    keyboard_press('Enter')

def navigate_to_account_orders(account_link_id, view_all_id):
    """Navigate from homepage to order history page.
    
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

def navigate_to_reviews_section(reviews_tab_id):
    """Navigate to the reviews section of a product page.
    
    Args:
        reviews_tab_id: The ID of the reviews tab element
        
    Returns:
        None
        
    Examples:
        navigate_to_reviews_section('1689')
    """
    click(reviews_tab_id)
    scroll(0, 300)