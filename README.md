### Frappe Cashfree

Integration for Frappe with Cashfree Payment gateway. 
This is a small integration solution for integrating Frappe with Cashfree. The dependencies of Python SDK of Cashfree has version clash with the dependencies of Frappe. Hence the need to write this app.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app frappe_cashfree
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/frappe_cashfree
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

MIT
