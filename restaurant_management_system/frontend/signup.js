document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signup-form');

    signupForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm-password').value;
        const role = document.getElementById('role').value;

        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        try {
            const response = await fetch('/api/auth/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: username,
                    email: email,
                    password: password,
                    role: role
                }),
            });

            if (response.ok) {
                // Optional: Show a non-blocking toast or just redirect
                window.location.href = 'login.html';
            } else {
                const data = await response.json();
                alert('Registration failed: ' + JSON.stringify(data));
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during registration.');
        }
    });
});
