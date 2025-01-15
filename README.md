<div align="center"> <a href="https://genezio.com/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/genez-io/graphics/raw/HEAD/svg/Icon_Genezio_White.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/genez-io/graphics/raw/HEAD/svg/Icon_Genezio_Black.svg">
    <img alt="genezio logo" src="https://github.com/genez-io/graphics/raw/HEAD/svg/Icon_Genezio_Black.svg" height="100" >
  </picture>
</a>
 </div>

<div align="center">

[![Join our community](https://img.shields.io/discord/1024296197575422022?style=social&label=Join%20our%20community%20&logo=discord&labelColor=6A7EC2)](https://discord.gg/uc9H5YKjXv)
[![Follow @geneziodev](https://img.shields.io/twitter/url/https/twitter.com/geneziodev.svg?style=social&label=Follow%20%40geneziodev)](https://twitter.com/geneziodev)

</div>

# Genezio Cron Python Getting Started

This is a simple example of how to create a cron job using Genezio and Python.

## Project Structure

- `index.py` - Contains the handler function that runs every hour, logging the execution time and returning a 200 status response
- `genezio.yaml` - Configuration file that defines the cron schedule and endpoint
- `requirements.txt` - Contains the dependencies for the project

## Cron Configuration

The cron job is configured to run every hour (at minute 0) using the cron expression `0 * * * *` in the `genezio.yaml` file, at the `/` endpoint.

## Function Details

The handler function:
- Prints the current execution time
- Logs any incoming event data

## Testing

You can test the endpoint manually by accessing it with your browser or using tools like curl/Postman.

# Deploy
:rocket: You can deploy your own version of the template to Genezio with one click:

[![Deploy to Genezio](https://raw.githubusercontent.com/Genez-io/graphics/main/svg/deploy-button.svg)](https://app.genez.io/start/deploy?repository=https://github.com/Genez-io/cron-python-getting-started)


## Genezio CLI Commands

Genezio also provides a CLI tool that you can use to deploy your project from your machine.
All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install -g genezio`  | Installs genezio globally                        |
| `genezio login`           | Logs in to genezio                               |
| `genezio local`           | Starts a local server                            |
| `genezio deploy`          | Deploys a production project                     |
| `genezio --help`          | Get help using genezio                           |

## Learn more

To learn more about Genezio, take a look at the following resources:

- [Official genezio documentation](https://genezio.com/docs)
- [Tutorials](https://genezio.com/blog)

## Contact

If you need support or you have any questions, please join us in our [Discord channel](https://discord.gg/uc9H5YKjXv). We'd love to chat!

## Built With

- [Genezio](https://genezio.com/)
- [Python](https://www.python.org/)

***

<div align="center"> <a href="https://genezio.com/">
  <p>Built with Genezio with ❤️ </p>
  <img alt="genezio logo" src="https://raw.githubusercontent.com/Genez-io/graphics/main/svg/powered_by_genezio.svg" height="40">
</a>
</div>