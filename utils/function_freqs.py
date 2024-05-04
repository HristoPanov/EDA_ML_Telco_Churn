import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class freqs:
    
    def feature_graph_freq(dataframe,feature,plot_kind):
        """
        Returns a plot of a feature and frequency table containing the # obs and % from total
        
        ob : please provide a DataFrame object 
        feature : please provide the name of the feature inside ''
        plot_kind : the type of the plot inside ''    
        """
        n_obs = dataframe[feature].value_counts(dropna=False)
        perc = round(dataframe[feature].value_counts(dropna=False, normalize=True)*100,2)
        graph = dataframe[feature].value_counts().plot(kind=plot_kind,color= 'tab:blue',figsize=(8, 4))
        plt.xlabel([feature])
        plt.ylabel("# of Observations")
        plt.title(feature)
        plt.show()
        return print("Cross Table {one} \n{two}".format(one=feature,two=pd.concat([n_obs,perc], axis=1, keys=['N_Obs', '% from Total'])))
    
    def plot_hist_two_ax(dataframe,variable,dependant,bins):
        """
        Returns the distribution graphic of a variable by the categories of "Churn".
        
        Parameters:
        dataset - Please probide a DataFrame inside ''
        variable - Please provide a int/float inside in ''
        """
        plt.figure(figsize=(8, 4))
        plt.title("Histogram of for {}".format(variable))
        ax0 = plt.hist(dataframe[dataframe[dependant] == 'No'][variable], color= 'tab:blue', label= f'{dependant} :No',bins=bins,edgecolor='black',alpha=0.9)
        ax1 = plt.hist(dataframe[dataframe[dependant] == 'Yes'][variable], color= 'tab:red', label= f'{dependant} :Yes',bins=bins,edgecolor='black',alpha=0.9)
        plt.legend()
        plt.xlabel('{}'.format(variable))
        plt.ylabel('# of Obs')
        
    def plot_count_fun(dataframe,variable,dependant):
        """
        Parameters:
        dataset : please provide a DataFrame object 
        variable : please provide the name of the feature inside ''  
        """    
        plt.figure(figsize=(8,6))
        sns.countplot(x=variable,data=dataframe,hue=dependant,palette='tab10')
        plt.tight_layout()
        plt.show()

    def plot_density_fun(dataframe,variable,variable_charges,dependant,bins):
        """
        Parameters:
        dataset : please provide a DataFrame object 
        variable : please provide the name of the feature inside '' 
        variable_charges: please provide the name of the feature representing charges inside ''
        """
        g = sns.FacetGrid(data=dataframe,col=dependant,row=variable,palette='tab10',height=3,aspect=2)
        g.map(sns.histplot,variable_charges,bins=bins,kde=True)
        plt.tight_layout()
        plt.show()