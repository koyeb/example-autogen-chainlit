<div align="center">
  <a href="https://koyeb.com">
    <img src="https://www.koyeb.com/static/images/icons/koyeb.svg" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Koyeb Serverless Platform</h3>
  <p align="center">
    Deploy an AutoGen and Chainlit application on Koyeb
    <br />
    <a href="https://koyeb.com">Learn more about Koyeb</a>
    ·
    <a href="https://koyeb.com/docs">Explore the documentation</a>
    ·
    <a href="https://koyeb.com/tutorials">Discover our tutorials</a>
  </p>
</div>

## About Koyeb and the AutoGen and Chainlit example application

Koyeb is a developer-friendly serverless platform to deploy apps globally. No-ops, servers, or infrastructure management.
This repository contains an AutoGen and Chainlit application you can deploy on the Koyeb serverless platform for testing.

This example application is designed to show how an AutoGen and Chainlit application can be deployed on Koyeb.

## Getting Started

Follow the steps below to deploy and run the AutoGen and Chainlit application on your Koyeb account.

### Requirements

You need a Koyeb account to successfully deploy and run this application. If you don't already have an account, you can sign-up for free [here](https://app.koyeb.com/auth/signup).

### Deploy using the Koyeb button

The fastest way to deploy the AutoGen and Chainlit application is to click the **Deploy to Koyeb** button below.

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/koyeb/example-autogen-chainlit&branch=main&name=autogen-on-koyeb)

Clicking on this button brings you to the Koyeb App creation page with everything pre-set to launch this application.

_To modify this application example, you will need to fork this repository. Check out the [fork and deploy](#fork-and-deploy-to-koyeb) instructions._

### Fork and deploy to Koyeb

If you want to customize and enhance this application, you need to fork this repository.

If you used the **Deploy to Koyeb** button, you can simply link your service to your forked repository to be able to push changes.
Alternatively, you can manually create the application as described below.

On the [Koyeb Control Panel](//app.koyeb.com/apps), click the **Create App** button to go to the App creation page.

1. Select `GitHub` as the deployment method to use
2. In the repositories list, select the repository you just forked
3. Specify the branch to deploy, in this case `main`
4. To let Koyeb know how to launch the application, add `chainlit run main.py` as the run command
5. Click **Advanced** to view additional settings. Click the **Add Variable** button to add your OpenAI API key named `OPENAI_API_KEY`.
6. Then, give your App a name, i.e `autogen-on-koyeb`, and click **Create App.**

You land on the deployment page where you can follow the build of your AutoGen and Chainlit application. Once the build is completed, your application is being deployed and you will be able to access it via `<YOUR_APP_NAME>-<YOUR_ORG_NAME>.koyeb.app`.

## Contributing

If you have any questions, ideas or suggestions regarding this application sample, feel free to open an [issue](//github.com//koyeb/example-autogen-chainlit/issues) or fork this repository and open a [pull request](//github.com/koyeb/example-autogen-chainlit/pulls).

## Contact

[Koyeb](https://www.koyeb.com) - [@gokoyeb](https://twitter.com/gokoyeb) - [Slack](http://slack.koyeb.com/)
