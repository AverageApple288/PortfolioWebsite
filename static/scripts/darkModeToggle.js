// Grab the button element from the DOM
var themeToggleBtn = document.getElementById('theme-toggle');
// Define a function to apply the theme
function setTheme(theme) {
    // Set the attribute on the <html> tag
    document.documentElement.setAttribute('data-theme', theme);
    // Save the choice to the browser's local storage
    localStorage.setItem('portfolio-theme', theme);
}
// Determine the initial theme on page load
function initializeTheme() {
    // Check if they already visited and saved a preference
    var savedTheme = localStorage.getItem('portfolio-theme');
    if (savedTheme) {
        setTheme(savedTheme);
    }
    else {
        // If no saved preference, check their OS/Browser system settings
        var systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        setTheme(systemPrefersDark ? 'dark' : 'light');
    }
}
// Run the initialization when the script loads
initializeTheme();
// Add the click event listener to the button
if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function () {
        // Check what the current theme is
        var currentTheme = document.documentElement.getAttribute('data-theme');
        // Toggle it
        if (currentTheme === 'dark') {
            setTheme('light');
        }
        else {
            setTheme('dark');
        }
    });
}
