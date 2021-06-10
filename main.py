import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

def main():
	
	activities = ["EDA","Plots"]
	choice = st.sidebar.selectbox("Select Activities",activities)

	if choice == 'EDA':
		st.subheader("Exploratory Data Analysis")
		st.write('**Created by Aryan Tanwar**')

		data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())

			if st.sidebar.checkbox("Show Shape"):
				st.write(df.shape)

			if st.sidebar.checkbox("Show Columns"):
				all_columns = df.columns.to_list()
				st.write(all_columns)

			if st.sidebar.checkbox("Summary"):
				st.write(df.describe())

			if st.sidebar.checkbox("Show Value Counts"):
				st.write(df.iloc[:,-1].value_counts())

			if st.sidebar.checkbox("Correlation Plot(Matplotlib)"):
				plt.matshow(df.corr())
				st.pyplot()

			if st.sidebar.checkbox("Correlation Plot(Seaborn)"):
				st.write(sns.heatmap(df.corr(),annot=True))
				st.pyplot()

			if st.sidebar.checkbox("Pie Plot"):
				all_columns = df.columns.to_list()
				column_to_plot = st.selectbox("Select 1 Column",all_columns)
				pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
				st.write(pie_plot)
				st.pyplot()



	elif choice == 'Plots':
		st.subheader("Data Visualization")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())

			if st.sidebar.checkbox("Show Value Counts"):
				st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
				st.pyplot()

			all_columns_names = df.columns.tolist()
			type_of_plot = st.sidebar.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
			selected_columns_names = st.sidebar.multiselect("Select Columns To Plot",all_columns_names)

			if st.sidebar.button("Generate Plot"):
				st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))


				if type_of_plot == 'area':
					cust_data = df[selected_columns_names]
					st.area_chart(cust_data)

				elif type_of_plot == 'bar':
					cust_data = df[selected_columns_names]
					st.bar_chart(cust_data)

				elif type_of_plot == 'line':
					cust_data = df[selected_columns_names]
					st.line_chart(cust_data)

				elif type_of_plot:
					cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
					st.write(cust_plot)
					st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

if __name__ == '__main__':
	main()

