// Open the default tab when the page loads
document.getElementById('profileTab').style.display = 'block';

let activeTab = 'profileTab';

function openTab(event, tabName) {
    // Get the tab content elements
    const tabContents = document.getElementsByClassName('tabcontent');
    for (const tabContent of tabContents) {
        tabContent.style.display = 'none';
    }

    // Get the tab link elements
    const tabLinks = document.getElementsByClassName('tablink');
    for (const tabLink of tabLinks) {
        tabLink.classList.remove('active');
    }

    // Display the selected tab content and set active tab styling
    document.getElementById(tabName).style.display = 'block';
    event.currentTarget.classList.add('active');
    activeTab = tabName;
}

let isGridView = true;

function toggleView() {
    const gridContainerProfiles = document.querySelector('#profileTab .grid-container');
    const cardItemsProfiles = document.querySelectorAll('#profileTab .card');

    const gridContainerPosts = document.querySelector('#postTab .grid-container');
    const cardItemsPosts = document.querySelectorAll('#postTab .card');

    const toggleButtonIcon = document.querySelector('.toggle-btn i');

    if (isGridView) {
        gridContainerProfiles.style.flexDirection = 'column';
        cardItemsProfiles.forEach(card => card.style.width = '100%');

        gridContainerPosts.style.flexDirection = 'column';
        cardItemsPosts.forEach(card => card.style.width = '100%');

        toggleButtonIcon.classList.remove('bx-list-ul');
        toggleButtonIcon.classList.add('bx-grid-alt');
    } else {
        gridContainerProfiles.style.flexDirection = 'row';
        cardItemsProfiles.forEach(card => card.style.width = '300px');

        gridContainerPosts.style.flexDirection = 'row';
        cardItemsPosts.forEach(card => card.style.width = '300px');

        toggleButtonIcon.classList.remove('bx-grid-alt');
        toggleButtonIcon.classList.add('bx-list-ul');
    }

    const tabContents = document.querySelectorAll('.tabcontent');
    tabContents.forEach(content => {
        if (isGridView) {
            content.classList.add('active');
        } else {
            content.classList.remove('active');
        }
    });

    isGridView = !isGridView;

}

