%% Import data from spreadsheet
% Script for importing data from the following spreadsheet:
%
%    Workbook: /Users/yaoruini/Downloads/MDM3-House/Education, Health, Entertainment by local district.xlsx
%    Worksheet: Table 1
%
% Auto-generated by MATLAB on 17-Mar-2022 22:12:24

%% Set up the Import Options and import the data
opts = spreadsheetImportOptions("NumVariables", 20);

% Specify sheet and range
opts.Sheet = "Table 1";
opts.DataRange = "A6:T375";

% Specify column names and types
opts.VariableNames = ["VarName1", "VarName2", "AgricultureForestryFishing", "Production", "Construction", "MotorTrades", "Wholesale", "Retail", "TransportStorageincPostal", "AccommodationFoodServices", "InformationCommunication", "FinanceInsurance", "Property", "ProfessionalScientificTechnical", "BusinessAdministrationSupportServices", "PublicAdministrationDefence", "Education", "Health", "ArtsEntertainmentRecreationOtherServices", "Total"];
opts.VariableTypes = ["string", "string", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double"];

% Specify variable properties
opts = setvaropts(opts, ["VarName1", "VarName2"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["VarName1", "VarName2"], "EmptyFieldRule", "auto");

% Import the data
EducationHealthEntertainmentbylocaldistrict = readtable("/Users/yaoruini/Downloads/MDM3-House/Education, Health, Entertainment by local district.xlsx", opts, "UseExcel", false);


%% Clear temporary variables
clear opts