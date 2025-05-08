# 🚦 Sliding-Window Rate Limiter

A distributed, accurate rate limiter using a sliding window algorithm backed by Redis. Designed to support multiple instances and handle edge cases like clock skew and Redis unavailability.

---

## 📌 Features

- ⏳ **Sliding Window Accuracy** — more precise than fixed buckets.
- 🧠 **Distributed Agreement** — Redis stores state to synchronize rate limits across instances.
- 🕒 **Handles Clock Skew** — server time differences don't break limits.
- 🔁 **Graceful Redis Failures** — safe fallback if Redis becomes unavailable.
- 🔑 **Client Identification** via `X-API-Key`.

---

## 🚀 API

### `GET /resource`

**Headers:**
```
X-API-Key: <client-id>
```

**Responses:**
- `200 OK`: Access granted.
- `429 Too Many Requests`: Rate limit exceeded.

---

## 🧪 How to Run

```bash
cd task2
docker-compose up
```

Then send traffic to:

```
http://localhost:8080/resource
```

Include the `X-API-Key` header to simulate different clients.

---

## 🔧 Testing Script

A Python script is included to send 200 requests/min and observe rate-limiting behavior. Modify the key to simulate different clients:

```bash
python fire_requests.py --rate 200 --key test-client
```

---

## 🛡️ Resilience Design

### Redis Failures
- If Redis is unreachable, fallback logic allows a limited number of requests (fail-open) to maintain basic functionality.
- Retries are applied with exponential backoff.

### Clock Skew
- Timestamps are managed centrally via Redis.
- Local server clocks do not impact correctness as long as they use Redis time (`TIME` command or ZSET scores).

---

## 🧱 Architecture

- Rate limiter middleware intercepts `/resource` requests.
- Uses Redis sorted sets (`ZADD`, `ZREMRANGEBYSCORE`, `ZCOUNT`) to track timestamps per client.
- Sliding window limit is enforced based on request timestamps.

---

## 📄 License

MIT License — free to use and modify.

---

## 👨‍💻 Author

by Shaikh M. Shaikh
