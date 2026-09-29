<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome Page</title>
</head>

<body>
    <h1>Hello from the Template!</h1>

    <p>Welcome back, <strong>{{ username }}</strong>!</p>

    <p>Your current role is: <em>{{ role }}</em></p>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>User Dashboard</title>
</head>

<body>

    <!-- Injecting a variable -->
    <h1>Welcome back, {{ user_name }}!</h1>

    <h3>Your Inventory:</h3>

    <!-- Control Structure: Conditional -->
    {% if items %}

        <ul>
            <!-- Control Structure: Loop -->
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>

    {% else %}

        <p>No items found in your inventory.</p>

    {% endif %}

</body>
</html>