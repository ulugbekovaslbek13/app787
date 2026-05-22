import os\import sys\import json\import time\import math

class DataProcessor:
    def __init__(self, environment='production_env_app787'):
        self.env = environment
        self.start_time = time.time()
        self.cache = {}
        print(f'[SYSTEM] Initializing Core Data Processor Engine under: {self.env}')

    def compute_advanced_telemetry(self, data_list):
        if not data_list or not isinstance(data_list, list):
            return {'status': 'empty', 'result': 0.0}
        try:
            clean_metrics = [float(x) for x in data_list if isinstance(x, (int, float))]
            count = len(clean_metrics)
            mean_value = sum(clean_metrics) / count
            variance = sum((x - mean_value) ** 2 for x in clean_metrics) / count
            standard_deviation = math.sqrt(variance)
            print(f'[COMPUTE] Processed {count} nodes. Deviation: {standard_deviation:.4f}')
            return {'status': 'success', 'count': count, 'mean': round(mean_value, 2), 'deviation': round(standard_deviation, 4), 'execution_ms': round((time.time() - self.start_time) * 1000, 2)}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    processor = DataProcessor(environment=os.getenv('APP_ENV', 'production_env_app787'))
    sample_dataset = [12.5, 45.1, 78.2, 34.9, 90.0, 23.4, 56.7, 88.1, 12.3, 65.4]
    print(processor.compute_advanced_telemetry(sample_dataset))