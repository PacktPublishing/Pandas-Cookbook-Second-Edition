import pandas as pd

import zipfile


def load_raw(zip_fname):
    with zipfile.ZipFile(zip_fname) as z:
        kag = pd.read_csv(z.open('multipleChoiceResponses.csv'))
        df = kag.iloc[1:]
    return df


def tweak_kag(df):
    na_mask = df.Q9.isna()
    hide_mask = df.Q9.str.startswith('I do not').fillna(False)
    df = df[~na_mask & ~hide_mask]
    
    q1 = (df.Q1
      .replace({'Prefer not to say': 'Another',
               'Prefer to self-describe': 'Another'})
      .rename('Gender')
    )
    q2 = df.Q2.str.slice(0,2).astype(int).rename('Age')
    def limit_countries(val):
        if val in  {'United States of America', 'India', 'China'}:
            return val
        return 'Another'
    q3 = df.Q3.apply(limit_countries).rename('Country')
   
    q4 = (df.Q4
     .replace({'Master’s degree': 18,
     'Bachelor’s degree': 16,
     'Doctoral degree': 20,
     'Some college/university study without earning a bachelor’s degree': 13,
     'Professional degree': 19,
     'I prefer not to answer': None,
     'No formal education past high school': 12})
     .fillna(11)
     .rename('Edu')
    )
    
    def only_cs_stat_val(val):
        if val not in {'cs', 'eng', 'stat'}:
            return 'another'
        return val
  
    q5 = (df.Q5
            .replace({
                'Computer science (software engineering, etc.)': 'cs',
                'Engineering (non-computer focused)': 'eng',
                'Mathematics or statistics': 'stat'})
             .apply(only_cs_stat_val)
             .rename('Studies'))
    def limit_occupation(val):
        if val in {'Student', 'Data Scientist', 'Software Engineer', 'Not employed',
                  'Data Engineer'}:
            return val
        return 'Another'
  
    q6 = df.Q6.apply(limit_occupation).rename('Occupation')
    
    q8 = (df.Q8
      .str.replace('+', '')
      .str.split('-', expand=True)
      .iloc[:,0]
      .fillna(-1)
      .astype(int)
      .rename('Experience')
    )
    
    q9 = (df.Q9
     .str.replace('+','')
     .str.replace(',','')
     .str.replace('500000', '500')
     .str.replace('I do not wish to disclose my approximate yearly compensation','')
     .str.split('-', expand=True)
     .iloc[:,0]
     .astype(int)
     .mul(1000)
     .rename('Salary'))
    return pd.concat([q1, q2, q3, q4, q5, q6, q8, q9], axis=1)
