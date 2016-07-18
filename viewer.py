import boto3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--group")
    parser.add_argument("--stream")
    args = parser.parse_args()

    log_reader = boto3.client('logs')
    next_token = None 

    while True:
        if next_token:
            response = log_reader.get_log_events(
                logGroupName=args.group,
                logStreamName=args.stream,
                nextToken=next_token,
                startFromHead=True,
            )
        else:
            response = log_reader.get_log_events(
	        logGroupName=args.group,
                logStreamName=args.stream,
                startFromHead=True,
            )

        next_token = response.get('nextForwardToken')
	events = response.get('events', [])

        if not len(events):
            break

        for event in events:
            print(event)
