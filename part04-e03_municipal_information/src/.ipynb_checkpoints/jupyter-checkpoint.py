{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: []\n",
       "Index: []"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame()\n",
    "df\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n"
     ]
    }
   ],
   "source": [
    "print(\"hello\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Region 2018\t\"Population\"\t\"Population change from the previous year</th>\n",
       "      <th>%\"\t\"Share of Swedish-speakers of the population</th>\n",
       "      <th>%\"\t\"Share of foreign citizens of the population</th>\n",
       "      <th>%\"\t\"Proportion of the unemployed among the labour force</th>\n",
       "      <th>%\"\t\"Proportion of pensioners of the population</th>\n",
       "      <th>%\"</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>WHOLE COUNTRY\\t5513130\\t0.2\\t5.2\\t4.5\\t13.5\\t25.3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Akaa\\t16769\\t-0.9\\t0.2\\t1.6\\t14.6\\t26.1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Alajärvi\\t9831\\t-0.7\\t0.1\\t1.9\\t13.9\\t32.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Alavieska\\t2610\\t-1.1\\t0.2\\t0.6\\t10.8\\t28.4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Alavus\\t11713\\t-1.6\\t0.1\\t1.1\\t11.3\\t31.5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Region 2018\\t\"Population\"\\t\"Population change from the previous year  \\\n",
       "0  WHOLE COUNTRY\\t5513130\\t0.2\\t5.2\\t4.5\\t13.5\\t25.3                     \n",
       "1            Akaa\\t16769\\t-0.9\\t0.2\\t1.6\\t14.6\\t26.1                     \n",
       "2         Alajärvi\\t9831\\t-0.7\\t0.1\\t1.9\\t13.9\\t32.0                     \n",
       "3        Alavieska\\t2610\\t-1.1\\t0.2\\t0.6\\t10.8\\t28.4                     \n",
       "4          Alavus\\t11713\\t-1.6\\t0.1\\t1.1\\t11.3\\t31.5                     \n",
       "\n",
       "    %\"\\t\"Share of Swedish-speakers of the population  \\\n",
       "0                                                NaN   \n",
       "1                                                NaN   \n",
       "2                                                NaN   \n",
       "3                                                NaN   \n",
       "4                                                NaN   \n",
       "\n",
       "    %\"\\t\"Share of foreign citizens of the population  \\\n",
       "0                                                NaN   \n",
       "1                                                NaN   \n",
       "2                                                NaN   \n",
       "3                                                NaN   \n",
       "4                                                NaN   \n",
       "\n",
       "    %\"\\t\"Proportion of the unemployed among the labour force  \\\n",
       "0                                                NaN           \n",
       "1                                                NaN           \n",
       "2                                                NaN           \n",
       "3                                                NaN           \n",
       "4                                                NaN           \n",
       "\n",
       "    %\"\\t\"Proportion of pensioners of the population   %\"  \n",
       "0                                               NaN  NaN  \n",
       "1                                               NaN  NaN  \n",
       "2                                               NaN  NaN  \n",
       "3                                               NaN  NaN  \n",
       "4                                               NaN  NaN  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"src/municipal.tsv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
