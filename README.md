# Real-time Order Aggregator

This project implements a real-time order processing system using Apache Kafka. It consists of a producer that generates sample order data and a consumer that processes and aggregates the orders.

## Project Structure

```
├── stream_processor.py  # Kafka consumer that processes and aggregates orders
├── stream_producer.py   # Kafka producer that generates sample order data
├── docker-compose.yaml  # Docker configuration for Kafka and Zookeeper
└── requirements.txt     # Python dependencies
```

## Features

- Real-time order processing
- High-value order detection and logging
- Periodic order statistics aggregation
- Sample order generation with random amounts and categories

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Start Kafka and Zookeeper using Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Usage

1. Start the order processor (consumer):
   ```bash
   python stream_processor.py
   ```

2. In a separate terminal, start the order producer:
   ```bash
   python stream_producer.py
   ```

## Configuration

- High-value order threshold: 200 (configurable in stream_processor.py)
- Statistics interval: 10 seconds (configurable in stream_processor.py)
- Order categories: books, electronics, fashion (configurable in stream_producer.py)

## Output

- High-value orders are logged to `high_value_orders.log`
- Aggregated statistics are saved to `order_stats.json` every 10 seconds

## License

MIT