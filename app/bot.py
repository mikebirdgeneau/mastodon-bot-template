from mastodon import Mastodon
import os
import logging

if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logger.info("Running bot.py")

    # Connect to Mastodon
    mdon = Mastodon(
        access_token=os.environ['MASTODON_ACCESS_TOKEN'],
        api_base_url=os.environ['MASTODON_API_BASE_URL'],
    )

    # Say hello!
    mdon.status_post(
        status="Hello world!",
    )

    logger.info("Done.")
