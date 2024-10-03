covid_data['case_month'] = pd.to_datetime(covid_data['case_month'])
covid_data['month_year'] = covid_data['case_month'].dt.to_period(
    'M').astype(str)
hospitalizations = covid_data[covid_data['hosp_yn'] == 'Yes']
deaths = covid_data[covid_data['death_yn'] == 'Yes']
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 8))
sns.kdeplot(hospitalizations['case_month'],
            label='Hospitalizations', ax=ax, color='blue', fill=True)
sns.kdeplot(deaths['case_month'], label='Deaths',
            ax=ax, color='red', fill=True)
ax.set_title(
    'KDE Plot of COVID-19 Hospitalizations and Deaths Over Time', fontsize=16)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Density', fontsize=14)
plt.xticks(rotation=45)
ax.legend()
plt.show()covid_data['case_month'] = pd.to_datetime(covid_data['case_month'])
covid_data['month_year'] = covid_data['case_month'].dt.to_period(
    'M').astype(str)
hospitalizations = covid_data[covid_data['hosp_yn'] == 'Yes']
deaths = covid_data[covid_data['death_yn'] == 'Yes']
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 8))
sns.kdeplot(hospitalizations['case_month'],
            label='Hospitalizations', ax=ax, color='blue', fill=True)
sns.kdeplot(deaths['case_month'], label='Deaths',
            ax=ax, color='red', fill=True)
ax.set_title(
    'KDE Plot of COVID-19 Hospitalizations and Deaths Over Time', fontsize=16)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Density', fontsize=14)
plt.xticks(rotation=45)
ax.legend()
plt.show()covid_data['case_month'] = pd.to_datetime(covid_data['case_month'])
covid_data['month_year'] = covid_data['case_month'].dt.to_period(
    'M').astype(str)
hospitalizations = covid_data[covid_data['hosp_yn'] == 'Yes']
deaths = covid_data[covid_data['death_yn'] == 'Yes']
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 8))
sns.kdeplot(hospitalizations['case_month'],
            label='Hospitalizations', ax=ax, color='blue', fill=True)
sns.kdeplot(deaths['case_month'], label='Deaths',
            ax=ax, color='red', fill=True)
ax.set_title(
    'KDE Plot of COVID-19 Hospitalizations and Deaths Over Time', fontsize=16)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Density', fontsize=14)
plt.xticks(rotation=45)
ax.legend()
plt.show()
