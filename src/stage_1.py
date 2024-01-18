import argparse
import yaml
import datetime
from logs import get_logger


def stage_1(config_path):
    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)
    logger = get_logger("STAGE1", log_level=config["base"]["log_level"])
    logger.info(config["stage-1"]["text"])
    with open(config["stage-1"]["output_filename"], "w") as text_file:
        text_file.write(f"Stage 1 complete at: {datetime.datetime.now()}")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()
    stage_1(config_path=args.config)
