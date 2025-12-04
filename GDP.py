import plotly.express as px

fig = px.bar(
    x=[30.3, 21.4, 4.9, 4.6, 4.3, 3.7, 3.3, 2.5, 2.3, 0.45],
    y=['USA','China','Germany','Japan','India','UK','France','Italy','Canada','Pakistan ⭐'],
    orientation='h',
    title='Top 10 GDP 2025 – Pakistan Rising Fast! توكلت على الله',
    color=[10,9,8,7,6,5,4,3,2,1],
    color_continuous_scale=['#00331a','#006633','#00994d','#00cc66','#00ff88']
)

fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='#00ff88',
    title_font_size=34,
    height=750,
    margin=dict(l=20, r=20, t=80, b=20)
)

fig.update_traces(
    texttemplate='%{x}T',
    textposition='outside',
    marker_line=dict(color='#00ff88', width=5)
)

fig.add_annotation(text="Pakistan Rising ⭐", x=0.45, y=9, showarrow=True, 
                   arrowcolor="#00ff88", font_size=26, font_color="#00ff88")

fig.add_annotation(text="توكلت على الله – 2030 تک Top 20 ان شاءاللہ", 
                   xref="paper", yref="paper", x=0.5, y=0.03, 
                   showarrow=False, font_size=20, font_color="#00ff88")

# Live HTML file banayega
fig.write_html("index.html")
print("Success! Live chart ready: index.html")
