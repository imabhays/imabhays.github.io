---
layout: single
title: "Day 01 - Setting Up Your Own Server in the Cloud"
excerpt: "Setting Up Your Own Server in the Cloud: A Step-by-Step Guide"
sidebar:
    nav: "linux21days"
header:
  teaser: /assets/images/bca/s3-dm-main.jpg
author_profile: false
categories: category-name
toc: true
toc_sticky: true
toc_label: "On This Page"
toc_icon: "list-ul"
tags:
  - linux
  - system admin
---

## Introduction
Hello! Today, I'll guide you through setting up a server in the cloud. With a plenty of hosting options available, both paid and free, the possibilities are indeed endless. Let's explore the AWS free tier server setup and start this 21 day Linux upskill challenge.

## Choosing the Right Server

Before we dive in, let's have a quick look at the options available:

- **Free Tiers**: AWS, Azure, Google Cloud Platform (GCP) offer free tiers, which are perfect for testing out your skills or running small, non-critical applications.
- **Paid Options**: Providers like Digital Ocean and Linode offer powerful options but come at a cost however the cost for basic plans is minimal though.
- **Local Server**: If you are keen to get hands-on experience, you can even set up a server locally, like on a Raspberry Pi. It will not if you're sitting behind NAT and you might need to invest in addional static IP address if you you need 

Now, let's set up a server on the AWS free tier.

> **Note**: To register for AWS Free Tier, you will need a credit card.

## Registering for AWS Free Tier

The AWS registration process is a straightforward, five-step process:

1. **Sign up**: Use your email to create your AWS account.
2. **Address**: Provide your contact address.
3. **Billing Info**: Input your credit card information.
4. **Identity Verification**: AWS will verify your identity through an SMS or voice call.
5. **Plan Selection**: Choose your plan and complete the signup.

After completing the registration, you will receive a confirmation email from AWS stating, "Your account is ready."  It usually takes 5 to 10 minutes.

## Launching Your First EC2 Instance

An EC2 compute instance is essentially a virtual server in the cloud. To set one up:

1. Log in to your AWS account as the root user.
2. Search for EC2, or navigate to Services > Compute > EC2.
3. Click on "Launch Instance."
4. Follow the instructions, entering the necessary details as prompted.

Congratulations! Your Ubuntu server is up and running. However, be mindful that your server is exposed to the whole internet at this stage.

## Accessing Your Server

To access your server, you can use a VM, the OpenSSH client in Windows 10, or Windows Subsystem for Linux (WSL). As a Linux Mint user on VMWare, here's my approach:

1. Locate the folder containing your .pem private key.
2. Adjust the file permissions with `sudo chmod 400 yourprivatekey.pem`.
3. Run SSH with the identity flag `ssh -i path_of_key username@public_ip4_address`. The default username for the ordinary user is 'ubuntu'.
4. Confirm to trust and save the IP in the known host list.

You should now see a command prompt displaying '$', indicating you're logged in as an ordinary user.

## Initial Server Setup

Now that we have access, let's perform the initial setup:

1. Update the server with `sudo apt update`.
2. Upgrade the server with `sudo apt upgrade`.

To logout, simply type 'logout' or 'exit'. In the next session, we'll set a password and run some basic commands.

## Conclusion

Setting up a server, especially an AWS free tier server setup, can seem daunting at first. But with this step-by-step guide, it becomes a breeze. While we have covered the basic AWS registration process and server setup, remember that the journey doesn't end here. Keep exploring, keep learning!

Slug: setting-up-your-first-cloud-server-with-aws-free-tier  
Meta description: Explore a comprehensive guide to setting up your first cloud server with AWS Free Tier. Learn the AWS registration process, how to launch an EC2 instance, and the steps to access it using an SSH client. A perfect read for beginners in cloud computing!
