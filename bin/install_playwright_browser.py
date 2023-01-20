import os, sys
python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)
browser = os.environ.get("PLAYWRIGHT_BUILDPACK_BROWSERS")
os.environ["PLAYWRIGHT_BROWSERS_PATH"]="/app/.heroku/python/lib/python" + python_version + "/site-packages/playwright/driver/package/.local-browsers/"
os.system("python -m playwright install " + browser)
