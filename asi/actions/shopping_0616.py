from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None

def search_nintendo_switch_storage(search_bar_id: str, num_cards: int):
    """Search for Nintendo Switch game card storage solutions.
    
    Args:
        search_bar_id: The ID of the search bar element
        num_cards: Number of cards that need to be stored
        
    Returns:
        None
        
    Examples:
        search_nintendo_switch_storage('567', 11)
        search_nintendo_switch_storage('179', 31)
    """
    click(search_bar_id)
    fill(search_bar_id, 'Nintendo Switch game card storage case')
    keyboard_press('Enter')

def navigate_to_account_orders(account_link_id: str):
    """Navigate to the order history page from account section.
    
    Args:
        account_link_id: The ID of the "My Account" link
        
    Returns:
        None
        
    Examples:
        navigate_to_account_orders('227')
    """
    click(account_link_id)
    click('1742')  # View All orders link

def access_product_reviews(reviews_tab_id: str):
    """Click on the reviews tab to access product reviews section.
    
    Args:
        reviews_tab_id: The ID of the reviews tab element
        
    Returns:
        None
        
    Examples:
        access_product_reviews('1576')
    """
    click(reviews_tab_id)

def search_for_product(search_bar_id: str, product_name: str):
    """Search for a product using the search bar.
    
    Args:
        search_bar_id: The ID of the search bar element
        product_name: The name or keywords of the product to search for
        
    Returns:
        None (performs search action)
        
    Examples:
        search_for_product('567', 'Nintendo Switch game card storage case')
        search_for_product('179', 'Nintendo Switch game card storage')
    """
    click(search_bar_id)
    fill(search_bar_id, product_name)
    keyboard_press('Enter')

def navigate_to_account_orders(account_link_id: str):
    """Navigate to the account orders page from homepage.
    
    Args:
        account_link_id: The ID of the "My Account" link
        
    Returns:
        None (navigates to orders page)
        
    Examples:
        navigate_to_account_orders('227')
    """
    click(account_link_id)
    click('1742')  # Click "View All" orders link

def browse_review_pages(reviews_tab_id: str):
    """Navigate through product review pages to read all reviews.
    
    Args:
        reviews_tab_id: The ID of the reviews tab element
        
    Returns:
        None (opens and navigates through reviews)
        
    Examples:
        browse_review_pages('1575')
    """
    click(reviews_tab_id)
    click('1990')  # Go to page 2
    click('2085')  # Return to page 1