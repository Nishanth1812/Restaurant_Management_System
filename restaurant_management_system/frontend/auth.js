async function login(username, password) {
    const response = await fetch('/api/auth/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);

        // Fetch user details to get role
        const userResponse = await fetch('/api/auth/me/', {
            headers: {
                'Authorization': `Bearer ${data.access}`
            }
        });

        if (userResponse.ok) {
            const userData = await userResponse.json();
            localStorage.setItem('user_role', userData.role);
            localStorage.setItem('user_name', userData.username);
        }

        window.location.href = 'index.html';
    } else {
        const errorData = await response.json();
        console.error('Login error:', errorData);
        alert('Login failed: ' + (errorData.detail || JSON.stringify(errorData)));
    }
}

function getUserRole() {
    return localStorage.getItem('user_role');
}

function logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_role');
    localStorage.removeItem('user_name');
    window.location.href = 'login.html';
}

function requireAuth() {
    if (!localStorage.getItem('access_token')) {
        window.location.href = 'login.html';
    }
}
