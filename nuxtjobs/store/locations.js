import exp from 'constants';
import { defineStore } from 'pinia'

const BASE_URL = 'http://127.0.0.1:8000';

export const useLocationsStore = defineStore('locations', {
    id: 'locations',
    state: () => ({
        locations: [],
        location: null,
        loading: false,
        error: null,
    }),
    getters: {
        allLocations: state => state.locations,
        locationsCount: state => state.locations.length,
        getLocation: state => state.location,
        isLoading: state => state.loading,
        getError: state => state.error,
        locationOptions: state => state.locations.map(location => ({
            name: location.name,
            slug: location.slug,
        })),
        locationNames: state => state.locations.map(location => location.name),
    },
    actions: {
        async fetchLocations() {
            this.loading = true;
            try {
                const response = await fetch(`${BASE_URL}/locations/`);
                const data = await response.json();
                this.locations = data;
            } catch (error) {
                this.error = error;
            } finally {
                this.loading = false;
            }
        },
        async fetchLocation(slug) {
            this.loading = true;
            try {
                const response = await fetch(`${BASE_URL}/locations/${slug}/`);
                const data = await response.json();
                this.location = data;
            } catch (error) {
                this.error = error;
            } finally {
                this.loading = false;
            }
        },
        async addLocation(location) {
            try {
                const response = await fetch(`${BASE_URL}/locations/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(location),
                });
                const data = await response.json();
                this.locations.push(data);
            } catch (error) {
                console.error(error);
                this.error = error.message;
            }
        },
        async updateLocation(location) {
            try {
                const response = await fetch(`${BASE_URL}/locations/${location.slug}/`, {
                    method: 'PUT',
                    headers: { 'content-type': 'application/json' },
                    body: JSON.stringify(location),
                });
                const data = await response.json();
                const index = this.locations.findIndex(location => location.slug === data.slug);
                this.locations[index] = data;
            } catch (error) {
                console.error(error);
                this.error = error.message;
            } finally {
                this.loading = false;
            }
        },
        async deleteLocation(location) {
            try {
                await fetch(`${BASE_URL}/locations/${location.slug}/`, {
                    method: 'DELETE',
                });
                this.locations = this.locations.filter(loc => loc.slug !== location.slug);
            } catch (error) {
                this.error = error.message;
            } finally {
                this.loading = false;
            }
        },
    },
});
