
# Feature Flag Service

This is a simple Node.js service for managing feature flags with user and region-specific overrides. The service allows for hot-reloading of flags from a `flags.json` file without restarting the server.

## Features

- **Feature Flags**: Allows enabling/disabling features globally, by region, or for specific users.
- **Hot-Reloading**: Automatically reloads flags from `flags.json` every time it changes.
- **Flag Evaluation**: Evaluate if a feature is enabled for a user in a given region.
- **Performance**: Evaluates flags in under 500 μs per request.

## Getting Started

### 1. Install Dependencies

First, make sure you have Node.js installed. Then, clone this repository and install the required dependencies:

```bash
npm install
```

### 2. Configuration

The flags are stored in the `flags.json` file. This file follows the structure:

```json
{
  "featureA": {
    "enabled": true,
    "overrides": {
      "users": {
        "42": false,
        "99": true
      },
      "regions": {
        "EU": true,
        "US": false
      }
    }
  },
  "featureB": {
    "enabled": false,
    "overrides": {
      "users": {},
      "regions": {
        "IN": true
      }
    }
  }
}
```

- **`featureA`**: Default is enabled, with user and region overrides.
- **`featureB`**: Default is disabled, with region-specific override.

### 3. Run the Service

To start the server, run:

```bash
node server.js
```

This will start the service on `http://localhost:9000`.

### 4. Test the API

To test the API, use `curl` or a browser:

```bash
curl "http://localhost:9000/flags?user=42&region=EU"
```

This will return the evaluation of feature flags for the given user and region:

```json
{
  "featureA": false,
  "featureB": false
}
```

### 5. Hot-Reloading Flags

Whenever you make changes to the `flags.json` file, the service will automatically reload the flags without requiring a restart.

### 6. Benchmarking

You can benchmark the performance of the API using **Autocannon**. First, install **Autocannon** globally:

```bash
npm install -g autocannon
```

Then run the following command to simulate 100 concurrent requests for 10 seconds:

```bash
autocannon -c 100 -d 10 -p 10 http://localhost:9000/flags?user=42&region=EU
```

### 7. Optimizations

If the latency is above 500 μs, consider:
- **Caching** the flags in memory.
- Using **asynchronous file reading** for non-blocking operations.

### 8. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

by Shaikh M. Shaikh
