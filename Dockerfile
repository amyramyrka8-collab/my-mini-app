# مرحلة البناء
FROM rust:1.75 as builder
WORKDIR /usr/src/app
COPY . .
RUN cargo build --release

# مرحلة التشغيل (خفيفة جداً)
FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y ca-certificates libssl-dev && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/src/app/target/release/okx_orderflow_bot /usr/local/bin/okx_orderflow_bot

# تشغيل البوت
CMD ["okx_orderflow_bot"]
