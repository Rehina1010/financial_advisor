def investment_recommendation(companies):
    recommendations = []
    for index, row in companies.iterrows():
        if row['Marketcap'] > 1e12:
            recommendations.append(f"Consider investing in {row['Shortname']} - {row['Sector']} sector.")
    return recommendations
