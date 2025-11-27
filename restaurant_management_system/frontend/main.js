// Main entry point
document.addEventListener('DOMContentLoaded', () => {
    const sidebarContainer = document.getElementById('sidebar-container');
    if (sidebarContainer) {
        fetch('components/sidebar.html')
            .then(res => res.text())
            .then(html => {
                sidebarContainer.innerHTML = html;
                
                // Highlight active link based on current URL
                const currentPath = window.location.pathname.split('/').pop() || 'index.html';
                const navId = 'nav-' + currentPath.replace('.html', '');
                const activeLink = document.getElementById(navId);
                if (activeLink) {
                    activeLink.classList.add('active');
                }

                // Role-based UI filtering
                const role = localStorage.getItem('user_role');
                if (role === 'STAFF') {
                    // Hide Inventory Link
                    const inventoryLink = document.getElementById('nav-inventory');
                    if (inventoryLink) inventoryLink.style.display = 'none';

                    // Hide Inventory Action (Dashboard)
                    const inventoryAction = document.getElementById('action-check-inventory');
                    if (inventoryAction) inventoryAction.style.display = 'none';

                    // Hide Update Menu Action (Dashboard) - Staff can VIEW menu but not UPDATE it via quick action if it implies editing
                    // If "Update Menu" leads to menu.html, we might want to keep it but rename it? 
                    // Or if menu.html is for both viewing and editing, we keep the link but restrict the page content.
                    // The user said "only the admin can add new items".
                    // Let's keep the dashboard link visible but restrict the "Add" button on the page.
                    // Actually, usually "Update Menu" implies editing. "Menu" implies viewing.
                    // Let's hide the "Update Menu" quick action to be safe, as they can access Menu via sidebar.
                    const updateMenuAction = document.getElementById('action-update-menu');
                    if (updateMenuAction) updateMenuAction.style.display = 'none';

                    // Hide "Add New Item" button on Menu Page
                    const addItemBtn = document.getElementById('btn-add-item');
                    if (addItemBtn) addItemBtn.style.display = 'none';

                    // Hide "Edit" buttons on Menu Page (using class)
                    // We need to do this AFTER the menu items are loaded. 
                    // Since menu items are loaded asynchronously, we might need a MutationObserver or handle it in menu.html
                    // For now, let's add a global style to hide them if body has a class 'role-staff'
                    document.body.classList.add('role-staff');
                }

                // Update Role Badge on Dashboard
                const roleBadge = document.getElementById('user-role-badge');
                if (roleBadge) {
                    roleBadge.innerText = role || 'Unknown';
                    if (role === 'ADMIN') {
                        roleBadge.style.background = 'rgba(236, 72, 153, 0.15)';
                        roleBadge.style.color = '#F472B6';
                        roleBadge.style.borderColor = 'rgba(236, 72, 153, 0.3)';
                    }
                }
            });
    }
});
