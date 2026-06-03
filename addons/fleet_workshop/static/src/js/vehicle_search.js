document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector(
        'input[name="search"]'
    );

    if (!searchInput) {
        return;
    }

    let timeout = null;

    searchInput.addEventListener('keyup', () => {

        clearTimeout(timeout);

        timeout = setTimeout(async () => {

            const response = await fetch(
                '/fleet/vehicles/search',
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        search: searchInput.value
                    })
                }
            );

            const result = await response.json();

            document.getElementById(
                'vehicle_results'
            ).innerHTML = result.result.html;

        }, 300);

    });

});