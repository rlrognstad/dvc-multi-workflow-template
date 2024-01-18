import argparse
import yaml
import datetime
from logs import get_logger


def stage_2a(config_path):
    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)
    logger = get_logger("STAGE2a", log_level=config["base"]["log_level"])
    logger.info(config["stage-2a"]["text"])
    with open(config["stage-1"]["output_filename"]) as input_file:
        lines = input_file.readlines()
    with open(config["stage-2a"]["output_filename"], "w") as output_file:
        for line in lines:
            output_file.write(line)
            output_file.write("\n")
        output_file.write(f"Stage 2a complete at: {datetime.datetime.now()}")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()
    stage_2a(config_path=args.config)
