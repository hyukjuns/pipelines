FROM hyukjun/myaspnet:3.1
WORKDIR /app
COPY ./app ./
ENV GlobalPassword=dkagh1.dkagh1.
ENV SimulatedFailureChance=0
ENTRYPOINT ["dotnet", "AnimalAdoption.Web.Portal.dll"]