{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "(unicode error) 'unicodeescape' codec can't decode bytes in position 3-4: truncated \\UXXXXXXXX escape (<ipython-input-6-6a156bd406bf>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-6-6a156bd406bf>\"\u001b[0;36m, line \u001b[0;32m3\u001b[0m\n\u001b[0;31m    df_original = pd.read_csv(\"src\\UK-top40-1964-1-2.tsv\",  sep =\"\\t\")\u001b[0m\n\u001b[0m                             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m (unicode error) 'unicodeescape' codec can't decode bytes in position 3-4: truncated \\UXXXXXXXX escape\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df_original = pd.read_csv(\"src/UK-top40-1964-1-2.tsv\",  sep =\"\\t\")\n",
    "    #df_final = \n",
    "print(df_original.head())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
