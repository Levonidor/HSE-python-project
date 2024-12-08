from kaggle.kaggle_read import *
from analytic.services import *
import streamlit as st
import plotly.express as px
from analytic.cfg import *
original_dataframe = create_dataframe()
main_dataframe = count_total_sales(original_dataframe)
sales_percentage_dataframe = create_sales_percentage_dataframe(original_dataframe)
total_sales_dataframe = create_total_sales_dataframe(main_dataframe)
count_games_by_publisher = create_games_by_publisher_dataframe(total_sales_dataframe)

st.title('Game sales analytic')


st.header('Overview')
st.write('**Original kaggle dataframe**')
st.write(original_dataframe)
st.write('Our data frame contains data about games with sales greater than 100,000 copies: their sales, on which platforms they were sold, by which publishers, year of release and in which markets how many were sold.')
st.write("Let's modify it to understand what percentage of the game's sales were in a particular market and how many copies of each game were sold in total from all platforms.")


if st.checkbox('Show **modificated dataframe for overview**'):
    st.write(sales_percentage_dataframe)
st.write('We have added data on the percentage of game sales in different regions. Now we will look at the various data and analyze it.')
spd_dataframes_ = spd_dataframes(original_dataframe)

spd_presentation_fig = px.bar(
    spd_dataframes_[0],
    x=ColNames.GENRE,
    y=ColNames.SALES,
    title='Sales by genre',
)
st.plotly_chart(spd_presentation_fig)
if st.checkbox('Show **sales by genre dataframe**'):
    st.write(spd_dataframes_[0])
st.write('As we can see, the best-selling games are games in the Action and Sports genres, the most unsold are Strategies.')


spd_presentation_fig = px.bar(
    spd_year_dataframe(original_dataframe),
    x=ColNames.YEAR,
    y=ColNames.GLOBAL_SALES,
    title='Sales per year'
)
st.plotly_chart(spd_presentation_fig)
if st.checkbox('Show **sales by year dataframe**'):
    st.write(spd_year_dataframe(original_dataframe))
st.write('Based on this bar chart, we see that the dataset does not contain enough information about 2016-2024. Excluding this fact, we are seeing a decrease in sales of games with more than 100,000 copies, therefore, since 2010, the number of sales of small indie projects that do not collect 100,000 copies has been growing, and large games that collect huge sales have become much less frequent.')
st.write("Next, we can look at the trend of sales of games in genres by year and you can draw the obvious conclusion yourself: the popularity of the genre is decreasing or increasing")
genre = st.selectbox(
    "Choose Genre:",
    genres_present
)
spd_presentation_fig = px.line(
    spd_dataframes_[1][spd_dataframes_[1][ColNames.GENRE] == genre],
    x=ColNames.YEAR,
    y=ColNames.SALES,
    title=f'Sales of {genre} per year',
)
st.plotly_chart(spd_presentation_fig)
if st.checkbox('Show **selected genre dataframe**'):
    st.write(spd_dataframes_[1][spd_dataframes_[1][ColNames.GENRE] == genre])
st.write('Here we notice an important point: the dataset does not contain enough information about 2016-2024, so a strong drawdown is noticed in all genres closer to our time. Therefore, we can make an unambiguous statement: all the analysis will be performed based on old data, and therefore something could have changed in our time.')

st.write("Now let's look at the average percentage of video game sales by region on specific platforms.")
st.write('**Percentages of PC, Xbox One and Playstation 3 sales by region**')
col1,col2,col3 = st.columns(3)
with col1:
    first = px.pie(
        spd_region_sales_dataframe(sales_percentage_dataframe,'PC'),
        values=ColNames.SALES,
        names=ColNames.REGION,
        title=f"PC", 
    )
    st.plotly_chart(first)
with col2:
    second = px.pie(
        spd_region_sales_dataframe(sales_percentage_dataframe,'XOne'),
        values=ColNames.SALES,
        names=ColNames.REGION,
        title=f"Xbox One ", 
    )
    st.plotly_chart(second)
with col3:
    third = px.pie(
        spd_region_sales_dataframe(sales_percentage_dataframe,'PS3'),
        values=ColNames.SALES,
        names=ColNames.REGION,
        title=f"Playstation 3", 
    )
    st.plotly_chart(third)
st.write('Following from these pie charts, it can be concluded that if a developer wants to sell his game mostly on the European market, he needs to develop it for the PC. If he wants to sell the game in America and Europe, his choice is Xbox. However, in order to sell the game worldwide, he needs to choose a Playstation.')
st.write('You can also check other platforms yourself and draw similar conclusions using the window below.')



platform = st.selectbox(
    "Choose Platform:",
    platforms_present
)
spd_presentation_fig = px.pie(
    spd_region_sales_dataframe(sales_percentage_dataframe,platform),
    values=ColNames.SALES,
    names=ColNames.REGION,
    title=f"Percentage of {platform} sales by region", 
)
st.plotly_chart(spd_presentation_fig)
if st.checkbox('Show **selected platform dataframe**'):
    st.write(spd_region_sales_dataframe(sales_percentage_dataframe,platform))




st.header('Deeper Overview')
tsd_presentation_fig = px.pie(
    create_first_tsd_presentation_dataframe(total_sales_dataframe),
    values=ColNames.TOTAL_SALES,
    names=ColNames.PUBLISHER,
    title="Publishers shares in the market", 
)
st.plotly_chart(tsd_presentation_fig)
if st.checkbox('Show **total sales of each game from all platforms dataframe**'):
    st.write(total_sales_dataframe)
st.write('*This pie chart puts all publishers with less than 1% of global sales in the "Others" category.*')
st.write('As we can see, 17.2% of global sales are from small publishers, while there are also hegemons such as Nintendo, whose sales account for 20.1% of global sales. Considering that there are a large number of companies in the video game market, it is estimated that the 5 largest publishers (*Nintendo, Electronic Arts, Activison, Sony Computer Entertainment and Ubisoft*) occupy the most number of players - 52.74%')
st.write("*Now let's look at the number of games released by different companies*")
tsd_presentation_fig = px.pie(
    create_second_tsd_presentation_dataframe(count_games_by_publisher),
    values=ColNames.TOTAL_COUNT,
    names=ColNames.PUBLISHER,
    title="Number of games by publisher", 
)
st.plotly_chart(tsd_presentation_fig)
if st.checkbox('Show **number of games by publisher dataframe**'):
    st.write(count_games_by_publisher)
st.write('Now we are witnessing the fact that the number of games released does not always lead to more sales. So Namco Bandai Games have made the most games among the major publishers, however (from the past pie chart) we see that their sales are 2.83%.')
st.write('It is also noticeable that independent (small) publishers release much more games (38.3% of all time) and at the same time their sales account for only 17.2% of the global total.')
st.write('In general, the following conclusion can be drawn from this: it is much more profitable to sell games through large publishers than through your own or small publishing companies. It also means that for a small company, the threshold for entering the video game market is quite high.')


st.title('Hypothesis')
st.write('**Hypothesis:** Games with global sales over 10 million are more likely to belong to the "Action" or "Shooter" genres than any other genres.',"*Let's check if this is true.*")

hypothesis_presentation_fig = px.pie(
    hypothesis(main_dataframe),
    values=ColNames.TOTAL_COUNT,
    names=ColNames.GENRE,
    title="Number of games with global sales over 10 million by genre", 
)
st.plotly_chart(hypothesis_presentation_fig)
if st.checkbox('Show **dataframe with Genre and its number of games with global sales over 10 million**'):
    st.write((hypothesis(main_dataframe)))
st.write('**The hypothesis is partially correct:** "Action" and "Shooter" are the most popular genres among over 10 million global sales games, but their dominance is not overwhelming compared to other genres: 34.4% of "Action"+"Shooter" againts 65.6% of other genres. Other genres, like "Role-Playing," "Sports," and "Platform," also contribute substantially to the list of games with over 10 million global sales.')
