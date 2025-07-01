# Real-time Order Aggregator with Kafka

A real-time order processing system built with Apache Kafka and Python, featuring a Streamlit dashboard for live analytics visualization.

## Features

- Real-time order processing with Kafka
- Live order statistics aggregation
- High-value order detection and logging
- Interactive dashboard with:
  - Real-time metrics display
  - Time series visualizations
  - Historical data tracking (30 minutes)
  - Recent orders table

## Architecture

```
├── stream_processor.py  # Kafka consumer for processing orders
├── stream_producer.py   # Kafka producer for generating orders
├── dashboard.py        # Streamlit dashboard for visualization
├── docker-compose.yaml # Docker configuration for Kafka
└── requirements.txt    # Python dependencies
```

## Prerequisites

- Python 3.x
- Docker and Docker Compose
- Git (for version control)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mohamed-amine-bouguerra-data-eng/Real-time-Order-Aggregator-with-Kafka.git
   cd Real-time-Order-Aggregator-with-Kafka
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start Kafka infrastructure:
   ```bash
   docker-compose up -d
   ```

## Usage

1. Start the order processor (consumer):
   ```bash
   python stream_processor.py
   ```

2. Launch the dashboard:
   ```bash
   streamlit run dashboard.py
   ```

3. Start generating orders (in a new terminal):
   ```bash
   python stream_producer.py
   ```

## Dashboard Features

- **Real-time Metrics**:
  - Order count (10-second intervals)
  - Revenue tracking
  - Time series visualizations

- **Historical Data**:
  - 30-minute history retention
  - Interactive charts
  - Recent orders table

## Configuration

- **Order Generator Settings** (stream_producer.py):
  - Order amount range: $5-$500
  - Categories: books, electronics, fashion
  - Generation interval: 0.5 seconds

- **Processor Settings** (stream_processor.py):
  - High-value threshold: $200
  - Statistics interval: 10 seconds

- **Dashboard Settings** (dashboard.py):
  - Update interval: 5 seconds
  - History retention: 30 minutes

## Error Handling

- Automatic reconnection to Kafka
- Data corruption detection
- User-friendly error messages
- Logging of high-value orders

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT