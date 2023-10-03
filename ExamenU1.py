{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMpy2RUFxgkFwXqkobyxEAi",
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
        "<a href=\"https://colab.research.google.com/github/madelavi/colab/blob/main/ExamenU1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "EduWKte5fGD6"
      },
      "outputs": [],
      "source": [
        "import math\n",
        "import random\n",
        "import string\n",
        "\n",
        "def primo(num):\n",
        "    if num < 2:\n",
        "        return False\n",
        "    for i in range(2, int(num**0.5) + 1, 2):\n",
        "        if num % i == 0:\n",
        "                return False\n",
        "    return True\n",
        "\n",
        "def next_primo(n):\n",
        "    sig_primo = n + 1\n",
        "    while True:\n",
        "        if primo(sig_primo):\n",
        "            return sig_primo\n",
        "        sig_primo += 1\n",
        "\n",
        "def mediana(a,b,c):\n",
        "  return sorted([a,b,c][1])\n",
        "\n",
        "def Contrasena():\n",
        "    longitud = random.randint(7, 10)\n",
        "    contrasena = \"\"\n",
        "    for _ in range(longitud):\n",
        "        caracter = chr(random.randint(33, 126))\n",
        "        contrasena += caracter\n",
        "    return contrasena\n",
        "\n",
        "def calc_hipotenusa(a,b):\n",
        "    hipotenusa = math.sqrt(a**2 + b**2)\n",
        "    return hipotenusa"
      ]
    }
  ]
}