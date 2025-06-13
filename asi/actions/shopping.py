from browsergym.core.action.functions import *

import playwright.sync_api
page: playwright.sync_api.Page = None

def navigate_to_reviews_section(reviews_tab_id: str):
    """Navigate to the reviews section of a product page.
    
    Args:
        reviews_tab_id: The ID of the reviews tab element
        
    Examples:
        navigate_to_reviews_section('1689')
    """
    click(reviews_tab_id)  # Click on the Reviews tab
    scroll(0, 300)  # Scroll down to see reviews content
    
def browse_all_review_pages(first_page_id: str, next_page_id: str):
    """Browse through multiple pages of reviews to see all content.
    
    Args:
        first_page_id: The ID of the first page link
        next_page_id: The ID of the next page link
        
    Examples:
        browse_all_review_pages('2199', '2483')
    """
    click(first_page_id)  # Click page 1 to start from beginning
    scroll(0, -500)  # Scroll up to see content
    click(next_page_id)  # Click to next page

def search_and_navigate_to_product(search_bar_id: str, product_name: str):
    """Search for a product and navigate to search results page.
    
    Args:
        search_bar_id: The ID of the search bar element
        product_name: The name or description of the product to search for
        
    Returns:
        None
        
    Examples:
        search_and_navigate_to_product('567', 'Nintendo Switch game card storage case')
        search_and_navigate_to_product('179', 'Nintendo Switch game card storage')
    """
    click(search_bar_id)
    fill(search_bar_id, product_name)
    keyboard_press('Enter')

def access_account_orders(account_link_id: str, view_all_id: str):
    """Navigate to account section and access order history.
    
    Args:
        account_link_id: The ID of the "My Account" link
        view_all_id: The ID of the "View All" orders link
        
    Returns:
        None
        
    Examples:
        access_account_orders('227', '1742')
    """
    click(account_link_id)
    click(view_all_id)

def search_and_enter_product(search_bar_id: str, product_name: str):
    """Search for a product using the search bar and press Enter.
    
    Args:
        search_bar_id: The ID of the search bar element
        product_name: The name or description of the product to search for
        
    Returns:
        None
        
    Examples:
        search_and_enter_product('567', 'Nintendo Switch game card storage case')
        search_and_enter_product('179', 'Nintendo Switch game card storage')
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

def navigate_order_pages_and_select(page_ids: list, order_link_id: str):
    """Navigate through multiple order pages and select a specific order.
    
    Args:
        page_ids: List of page link IDs to navigate through
        order_link_id: The ID of the specific order to view
        
    Returns:
        None
        
    Examples:
        navigate_order_pages_and_select(['1816', '1824'], '1701')
    """
    for page_id in page_ids:
        click(page_id)
    click(order_link_id)

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

def navigate_to_order_details(account_link_id: str):
    """Navigate from homepage to account order history.
    
    Args:
        account_link_id: The ID of the "My Account" link
        
    Returns:
        None
        
    Examples:
        navigate_to_order_details('227')
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
        access_product_reviews('1689')
    """
    click(reviews_tab_id)