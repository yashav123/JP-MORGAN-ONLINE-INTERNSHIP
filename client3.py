{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOLk/e4DVlIli98T0f956G6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yashav123/JP-MORGAN-ONLINE-INTERNSHIP/blob/main/client3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AnZOXtGhBCly",
        "outputId": "f6c3e000-54f5-4e48-eafb-f1d234954435"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "I'm a car!\n",
            "What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?67\n",
            "I don't know how to do that\n",
            "What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?56\n",
            "I don't know how to do that\n"
          ]
        }
      ],
      "source": [
        "class Car:\n",
        "\n",
        "    def __init__(self, speed=0):\n",
        "        self.speed = speed\n",
        "        self.odometer = 0\n",
        "        self.time = 0\n",
        "\n",
        "    def accelerate(self):\n",
        "        self.speed += 5\n",
        "\n",
        "    def brake(self):\n",
        "        self.speed -= 5\n",
        "\n",
        "    def step(self):\n",
        "        self.odometer += self.speed\n",
        "        self.time += 1\n",
        "\n",
        "    def average_speed(self):\n",
        "        return self.odometer / self.time\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "\n",
        "    my_car = Car()\n",
        "    print(\"I'm a car!\")\n",
        "    while True:\n",
        "        action = input(\"What should I do? [A]ccelerate, [B]rake, \"\n",
        "                        \"show [O]dometer, or show average [S]peed?\").upper()\n",
        "        if action not in \"ABOS\" or len(action) != 1:\n",
        "            print(\"I don't know how to do that\")\n",
        "            continue\n",
        "        if action == 'A':\n",
        "            my_car.accelerate()\n",
        "            print(\"Accelerating...\")\n",
        "        elif action == 'B':\n",
        "            my_car.brake()\n",
        "            print(\"Braking...\")\n",
        "        elif action == 'O':\n",
        "            print(\"The car has driven {} kilometers\".format(my_car.odometer))\n",
        "        elif action == 'S':\n",
        "            print(\"The car's average speed was {} kph\".format(my_car.average_speed()))\n",
        "        my_car.step()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "loGK2ow0FKzd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "pzLbwtRNBHGS"
      }
    }
  ]
}